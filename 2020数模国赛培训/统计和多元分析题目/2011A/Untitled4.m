clc; clear all; close all;
% 文件名称
filename = 'cumcm2011A附件_数据.xls';
% 读取附件1、2的数据
[num1, txt1, raw1] = xlsread(filename, '附件1');
[num2, txt2, raw2] = xlsread(filename, '附件2');
% 提取有效数据
A = num1(:, 2:4);
B = num2(:, 2:9);
% 获取三维点信心
x = A(:, 1);
y = A(:, 2);
z = A(:, 3);
% 获取第一个金属的值
% co = B(:, 1);
co = num1(:, 5);
% 网格数据
[xt, yt] = meshgrid(linspace(min(x), max(x)), linspace(min(y), max(y)));
% 网格插值——节点
zt = griddata(x, y, z, xt, yt, 'v4');
% 网格插值——颜色
cot = griddata(x, y, co, xt, yt, 'v4');
% 绘图
figure; hold on; box on;
plot3(x, y, z, 'r.');
surf(xt, yt, zt, cot);
view(3)
colorbar
colormap([0 0 0; 0.1 0.5 0.4; 0.2 0.2 0.6; 0.3 0.3 0.4; 0 1 0; 0 0.5 0.5; 0 0 1])