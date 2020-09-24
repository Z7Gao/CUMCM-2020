clc; clear all; close all;
filename = 'cumcm2011A����_����.xls';
[num1, txt1, raw1] = xlsread(filename, '����1');
A = num1(:, 2:4);
x = A(:, 1);
y = A(:, 2);
z = A(:, 3);
% ��������
[xt, yt] = meshgrid(linspace(min(x), max(x)), linspace(min(y), max(y)));
% �����ֵ�����ڵ�
zt = griddata(x, y, z, xt, yt, 'v4');
figure; hold on; box on;
surf(xt, yt, zt);