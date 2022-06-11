#ifndef __OL113STACK_H__
#define __OL113STACK_H__

/*  version 4  */

#include <stddef.h> /* size_t */

typedef struct stack stack_t;

stack_t *StackCreate(size_t num_of_elements);
void StackDestroy(stack_t *stack_ptr);
void StackPop(stack_t *stack_ptr);
void StackPush(stack_t *stack_ptr, void *element_ptr);
void *StackPeek(stack_t *stack_ptr);
size_t StackSize(const stack_t *stack_ptr);
int StackIsEmpty(const stack_t *stack_ptr);
size_t StackCapacity(const stack_t *stack_ptr);

#endif /* __OL113STACK_H__ */

