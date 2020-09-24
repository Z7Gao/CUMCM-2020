clc; clear all; close all;
% �ļ�����
filename = 'cumcm2011A����_����.xls';
% ��ȡ����1��2������
[num1, txt1, raw1] = xlsread(filename, '����1');
[num2, txt2, raw2] = xlsread(filename, '����2');
% ��ȡ��Ч����
A = num1(:, 2:4);
B = num2(:, 2:9);
% ��ȡ��ά������
x = A(:, 1);
y = A(:, 2);
z = A(:, 3);
% ��ȡ��һ��������ֵ
% co = B(:, 1);
co = num1(:, 5);
% ��������
[xt, yt] = meshgrid(linspace(min(x), max(x)), linspace(min(y), max(y)));
% �����ֵ�����ڵ�
zt = griddata(x, y, z, xt, yt, 'v4');
% �����ֵ������ɫ
cot = griddata(x, y, co, xt, yt, 'v4');
% ��ͼ
figure; hold on; box on;
plot3(x, y, z, 'r.');
surf(xt, yt, zt, cot);
view(3)
colorbar
colormap([0 0 0; 0.1 0.5 0.4; 0.2 0.2 0.6; 0.3 0.3 0.4; 0 1 0; 0 0.5 0.5; 0 0 1])