% Comprueba si estamos ejecutando en MATLAB o en OCTAVE_EXEC_HOME
if exist('OCTAVE_VERSION', 'builtin') ~= 0
    % Estamos en OCTAVE
    pkg load signal;
end

% Menú principal
opcion = 0;

while opcion ~= 5
    % Menú de opciones
    disp('Seleccione una opcion:');
    disp('1. Grabar');
    disp('2. Reproducir');
    disp('3. Graficar');
    disp('4. Graficar densidad');
    disp('5. Salir');

    opcion = input('Ingrese su elección: ');

    switch opcion
        case 1
            % Grabacion de audio
            try
                duracion = input('Ingrese la duracion de la grabacion en segundos: ');
                disp('Comenzando la grabacion...');
                recObj = audiorecorder;
                recordblocking(recObj, duracion);
                disp('Grabacion finalizada.');
                data = getaudiodata(recObj);
                audiowrite('audio.wav', data, recObj.SampleRate);
                disp('Archivo de audio guardado correctamente.');
            catch
                disp('Error al grabar audio.');
            end
        case 2
            % Reproduccion de audio
            try
                [data, fs] = audioread('audio.wav');
                sound(data, fs);
            catch
                disp('Error al reproducir el audio.');
            end
        case 3
            % Grafico de audio
            try
                [data, fs] = audioread('audio.wav');
                tiempo = linspace(0, length(data) / fs, length(data));
                plot(tiempo, data);
                xlabel('Tiempo (s)');
                ylabel('Amplitud');
                title('Audio');
            catch
                disp('Error al graficar audio.');
            end
        case 4
            % Graficando el espectro de frecuencia
            try
                disp('Graficando el espectro de frecuencia...');
                [audio, Fs] = audioread('audio.wav'); % Lee las señales del archivo wav
                N = length(audio); % Numero de muestras de señal
                f = linspace(0, Fs / 2, N / 2 + 1); % Vector de frecuencias
                ventana = hann(N); % Ventana de Hann para reducir el efecto de las discontinuidades
                Sxx = pwelch(audio, ventana, 0, N, Fs); % Densidad espectral de potencia
                plot(f, 10 * log10(Sxx(1:N / 2 + 1))); % Grafica el espectro de frecuencia en dB
                xlabel('Frecuencia (Hz)');
                ylabel('Densidad espectral de potencia (dB/Hz)');
                title('Espectro de frecuencia de la señal grabada');
            catch
                disp('Error al graficar el audio.');
            end
        case 5
            % Salir
            disp('Saliendo del programa');
        otherwise
            disp('Opcion no válida.');
    end
end

