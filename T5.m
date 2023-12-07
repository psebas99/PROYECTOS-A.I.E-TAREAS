% Verifica si la variable 'OCTAVE_VERSION' está definida y si es Octave,
% carga el paquete de señales.
if(exist('OCTAVE_VERSION','builtin')~=0)
    pkg load signal;
end

% Menú principal
opcion = 0;
while opcion ~= 5
    disp('Seleccione una opcion')
    disp('1. Grabar')
    disp('2. Reproducir')
    disp('3. Graficar')
    disp('4. Graficar densidad')
    disp('5. Salir')

    opcion = input('Ingrese su elección:');

    switch opcion
        case 1
            try
                % Opción para grabar audio
                duracion = input('Ingrese la duración de la grabación en segundos:');
                disp('Comenzando la grabación');
                recObj = audiorecorder;
                recordblocking(recObj, duracion);
                disp('Grabación finalizada');
                data = getaudiodata(recObj);
                audiowrite('audio.wav', data, recObj.SampleRate);
                disp('Archivo de audio grabado correctamente');
            catch
                disp('Error al grabar audio');
            end
        case 2
            try
                % Opción para reproducir audio
                [data, fs] = audioread('audio.wav');
                sound(data, fs);
            catch
                disp('Error al reproducir el audio');
            end
        case 3
            try
                % Opción para graficar la forma de onda del audio
                [data, fs] = audioread('audio.wav');
                tiempo = linspace(0, length(data)/fs, length(data));
                plot(tiempo, data);
                xlabel('Tiempo(s)');
                ylabel('Amplitud');
                title('Audio');
            catch
                disp('Error al graficar el audio');
            end
        case 4
            try
                % Opción para graficar el espectro de frecuencia
                disp('Graficando espectro de frecuencia');
                [audio, Fs] = audioread('audio.wav');
                N = length(audio);
                f = linspace(0, Fs/2, N/2+1);
                ventana = hann(N);
                Sxx = pwelch(audio, ventana, 0, N, Fs);
                plot(f, 10*log10(Sxx(1:N/2+1)));
                xlabel('Frecuencia (Hz)');
                ylabel('Densidad espectral de potencia(dB/Hz)');
                title('Espectro de frecuencia de la señal grabada');
            catch
                disp('Error al graficar el audio');
            end
        case 5
            % Opción para salir del programa
            disp('Saliendo del programa');
            break
        otherwise
            % Opción inválida
            disp('Opción inválida');
    end
end

