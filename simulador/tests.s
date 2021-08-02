.text
main: mov r0, #0 @ Total a 0
mov r1, #10 @ Inicializa n a 10
loop: mov r2, r1 @ Copia n a r2
mul r2, r1 @ Almacena n al cuadrado en r2
mul r2, r1 @ Almacena n al cubo en r2
add r0, r0, r2 @ Suma [r0] y el cubo de n
sub r1, r1, #1 @ Decrementa n en 1
bne loop @ Salta a «loop» si n != 0
stop: wfi
.end