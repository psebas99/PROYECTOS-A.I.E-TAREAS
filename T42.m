n = -1000:1000;
x = exp(j * 2 * pi * 0.01 * n);
y = exp(j * 2 * pi * 2.01 * n);

figure;
plot(n, real(x), 'b', n, real(y), 'r');
grid on;
title('Parte Real de las señales');
xlabel('n');
ylabel('Parte Real');
legend('x: 0.01 Hz', 'y: 2.01 Hz');

