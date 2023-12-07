t = -0.04:0.001:0.04;
x = 20 * exp(j * (80 * pi * t - 0.4 * pi));

% Gráfica 3D
figure;
plot3(t, real(x), imag(x));
grid on;
title('Gráfica 3D: 20 * e^{j*(80\pit-0.4\pi)}');
xlabel('Tiempo, s');
ylabel('Parte Real');
zlabel('Parte Imaginaria');

% Gráfica 2D de las partes real e imaginaria
figure;
plot(t, real(x), 'b', t, imag(x), 'r');
grid on;
title('Parte Real (azul) e Imaginaria (rojo) de 20 * e^{j*(80\pit-0.4\pi)}');
xlabel('Tiempo, s');
ylabel('Amplitud');
legend('Real', 'Imaginaria');

