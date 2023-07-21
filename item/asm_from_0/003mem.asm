global main

main:
	mov eax, [num1]
	mov ebx, [num2]
	add eax, ebx
	ret

section .data
num1	dw	10
num2	dw	20
