#include "stack.h"
#include <stdlib.h> /* malloc */
#include <assert.h> /* assert */

struct stack
{
	void **arr;
	size_t max_size;
	size_t top_index;
};

stack_t *StackCreate(size_t num_of_elements)
{
	stack_t *stack_ptr = malloc(sizeof(stack_t));
	
	if (!stack_ptr)
	{
		return NULL;
	}
	
	stack_ptr->arr = (void **)malloc(num_of_elements * sizeof(void *));

	if (!(stack_ptr->arr))
	{
		free(stack_ptr);
		
		return NULL;
	}
	
	stack_ptr->max_size = num_of_elements;
	stack_ptr->top_index = 0;
	
	return stack_ptr;
}

void StackDestroy(stack_t *stack_ptr)
{
	assert(stack_ptr);

	free(stack_ptr->arr);
	stack_ptr->arr = NULL;
	
	free(stack_ptr);
	stack_ptr = NULL;
}

void StackPush(stack_t *stack_ptr, void *element_ptr)
{
	assert(stack_ptr);
	
	stack_ptr->arr[stack_ptr->top_index] = element_ptr;
	stack_ptr->top_index++;
}

void StackPop(stack_t *stack_ptr)
{
	assert(stack_ptr);
	
	stack_ptr->top_index--;
}

void *StackPeek(stack_t *stack_ptr)
{
	assert(stack_ptr);
	
	return stack_ptr->arr[stack_ptr->top_index - 1];
}

size_t StackSize(const stack_t *stack_ptr)
{
	assert(stack_ptr);
	
	return stack_ptr->top_index;
}

int StackIsEmpty(const stack_t *stack_ptr)
{
	return 0 == stack_ptr->top_index;
}

size_t StackCapacity(const stack_t *stack_ptr)
{
	return stack_ptr->max_size;
}
