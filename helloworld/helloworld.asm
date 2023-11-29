section .data
    hello db 'Olá, mundo!',0

section .text
    global _start

_start:
    ; Escrever a string no stdout
    mov eax, 4          
    mov ebx, 1         
    mov ecx, hello     
    mov edx, 13         
    int 0x80            

    ; Sair do programa
    mov eax, 1          
    xor ebx, ebx        
    int 0x80            
