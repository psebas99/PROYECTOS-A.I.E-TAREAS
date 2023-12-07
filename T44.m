% Definición de la variable n
n = -3:0.1:7; % Crear un vector de -3 a 7 con paso de 0.1
x = 0.55 .^ (n + 3); % Definir la señal x

% Definición de la respuesta al impulso h
h = [1 1 1 1 1 1 1 1 1 1 1]; % Respuesta al impulso h

% Realizar la convolución de x y h
y = conv(x, h);

% Subplot 1: Gráfica de la señal original x
subplot(3, 1, 1);
stem(n, x, 'r'); % Usar 'r' para especificar el color rojo
title('Señal original');
xlabel('n');
ylabel('Amplitud');

% Subplot 2: Gráfica de la respuesta al impulso h
subplot(3, 1, 2);
stem(0:length(h)-1, h, 'g'); % Usar 'g' para especificar el color verde
title('Respuesta al impulso');
xlabel('n');
ylabel('Amplitud');

% Subplot 3: Gráfica de la convolución resultante y
subplot(3, 1, 3);
stem(0:length(y)-1, y, 'b'); % Usar 'b' para especificar el color azul
title('Convolución resultante');
xlabel('n');
ylabel('Amplitud');

