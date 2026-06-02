#!/usr/bin/perl

use strict;
use warnings;

my @my_names = (
    "Fu, X.", "Xiaokang Fu", "Fu, Xiaokang", "付小康",
    # 如果有带dagger的显示，也在这里添加
    "Fu†, X.", "Fu†, Xiaokang", "Fu†, 付小康"
);

# 构建替换的正则表达式
my $name_regex = join("|", map { quotemeta($_) } @my_names);
$name_regex = qr/($name_regex)/;

# 从命令行参数获取文件列表
my @files = @ARGV;

foreach my $file (@files) {
    next unless -f $file; # 确保是文件
    
    my $content;
    open(my $fh, '<:encoding(UTF-8)', $file) or die "Cannot open $file: $!";
    {
        local $/; # 切换到“段落模式”，一次读完整个文件
        $content = <$fh>;
    }
    close $fh;

    # 进行替换，使用 <strong> 标签加粗
    $content =~ s/$name_regex/<strong>$1<\/strong>/g;

    open(my $fh_out, '>:encoding(UTF-8)', $file) or die "Cannot write to $file: $!";
    print $fh_out $content;
    close $fh_out;
    
    print "Processed $file\n";
}
