clear


% tasso di interesse nom. o eff.

scelta_tasso = menu('Seleziona il tipo di tasso di interesse/sconto', ...
                    'Effettivo (i già noto)', ...
                    'Nominale ( → calcolo i effettivo)');

if scelta_tasso == 1
    % ieff noto
    i = input('Inserisci il tasso effettivo i = ');
else
    % calcolo ieff
    r = input('Inserisci il tasso nominale = ');
    m = input('Inserisci il numero di composizioni ');
    I = input('Inserisci la durata del periodo in anni ');
    
    i = (1 + r/m)^(m*I) - 1;
    fprintf('Tasso effettivo calcolato: %.4f\n', i);
end


n = input('Inserisci orizzonte investimento');


% fattori per prestazione multipla o singola

F_P = (1 + i)^n;
P_F = 1 / (1 + i)^n;
A_P = (i * (1 + i)^n) / ((1 + i)^n - 1);
P_A = ((1 + i)^n - 1) / (i * (1 + i)^n);
F_A = ((1 + i)^n - 1) / i;
A_F = i / ((1 + i)^n - 1);


fprintf('F/P : %.4f\n', F_P);
fprintf('P/F : %.4f\n', P_F);
fprintf('A/P : %.4f\n', A_P);
fprintf('P/A : %.4f\n', P_A);
fprintf('F/A : %.4f\n', F_A);
fprintf('A/F : %.4f\n\n', A_F);


% menu incognita

inc_index = menu('Quale grandezza vuoi calcolare?', 'P', 'F', 'A');
incognita = ['P','F','A'];
inc = incognita(inc_index);


% menu nota

while true
    var_index = menu('Quale grandezza conosci?', 'P', 'F', 'A');
    nota = incognita(var_index);
    
    if inc ~= nota
        break;
    else
        msgbox('Non puoi scegliere la stessa variabile!','Errore','error');
    end
end


val = input(['Inserisci il valore di ', nota, ' = ']);

%calcoli per risultato di output

switch inc
    
    case 'F'
        if nota == 'P'
            F = val * F_P;
            formula = 'F = P * (F/P)';
        elseif nota == 'A'
            F = val * F_A;
            formula = 'F = A * (F/A)';
        end
        fprintf('\n%s\n', formula);
        fprintf('Risultato: F = %.4f\n', F);

    case 'P'
        if nota == 'F'
            P = val * P_F;
            formula = 'P = F * (P/F)';
        elseif nota == 'A'
            P = val * P_A;
            formula = 'P = A * (P/A)';
        end
        fprintf('\n%s\n', formula);
        fprintf('Risultato: P = %.4f\n', P);

    case 'A'
        if nota == 'P'
            A = val * A_P;
            formula = 'A = P * (A/P)';
        elseif nota == 'F'
            A = val * A_F;
            formula = 'A = F * (A/F)';
        end
        fprintf('\n%s\n', formula);
        fprintf('Risultato: A = %.4f\n', A);
end