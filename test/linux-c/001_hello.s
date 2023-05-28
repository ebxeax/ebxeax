.section .data
.section .text
.globl _start
_start:
       movl $1, %eax
       movl $111, %ebx
       int $0x80

# int : interupt 软中断指令，产生异常，CPU从用户模式切换为特权模式，跳转到内核代码中执行异常处理程序
# eax : 系统调用号 1:_exit
# ebx : 传递给_exit的值
