% Definición del vector n
n = -50:50;

% Definición de las señales x, y, z
x = cos(pi * 0.1 * n);
y = cos(pi * 0.9 * n);
z = cos(pi * 2.1 * n);

% Subplot 1: Gráfica de la señal x
subplot(3, 1, 1);
plot(n, x);
title('y[n] = cos(0.1\pin)'); % Título de la gráfica
grid on; % Habilitar cuadrícula en la gráfica

% Subplot 2: Gráfica de la señal y
subplot(3, 1, 2);
plot(n, y);
title('y[n] = cos(0.9\pin)'); % Título de la gráfica
grid on; % Habilitar cuadrícula en la gráfica

% Subplot 3: Gráfica de la señal z
subplot(3, 1, 3);
plot(n, z);
title('z[n] = cos(2.1\pin)'); % Título de la gráfica
grid on; % Habilitar cuadrícula en la gráfica

% Etiqueta global para el eje x
xlabel('n');

