/* Reviewer- Shira */

#include "vector.h"
#include <stdlib.h> /* malloc realloc free */
#include <assert.h> /* assert */
#include <string.h> /* memcpy */

struct dynamic_vector
{
	void *arr;
	size_t last_index;
	size_t num_elements;
	size_t element_size;
};

enum status {SUCCESS, FAIL_REALLOC};

vector_t *VectorCreate(size_t num_elements, size_t element_size)
{
	vector_t *vector_ptr = NULL;

	assert(num_elements && element_size);
	
	vector_ptr = malloc(sizeof(vector_t));
	
	if (!vector_ptr)
	{
		return NULL;
	}
	
	vector_ptr->arr = malloc(num_elements * element_size);

	if (!(vector_ptr->arr))
	{
		free(vector_ptr);
		vector_ptr = NULL;
		
		return NULL;
	}
	
	vector_ptr->last_index = 0;
	vector_ptr->num_elements = num_elements;
	vector_ptr->element_size = element_size;
	
	return vector_ptr;
}

void VectorDestroy(vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	free(vector_ptr->arr);
	vector_ptr->arr = NULL;
	
	free(vector_ptr);
	vector_ptr = NULL;
}

void VectorPopBack(vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	vector_ptr->last_index--;
}

int VectorPushBack(vector_t *vector_ptr, const void *val)
{
	char *address_to_cpy = NULL;
	
	assert(vector_ptr);
	
	if (vector_ptr->last_index == vector_ptr->num_elements)
	{
		if (VectorReserve(vector_ptr, vector_ptr->num_elements * 2))
		{
			return 1;
		}
	}
	
	address_to_cpy = vector_ptr->arr;
	address_to_cpy += vector_ptr->last_index * vector_ptr->element_size;
	memcpy(address_to_cpy, val, vector_ptr->element_size);
	vector_ptr->last_index++;
	
	return 0;
}

void *VectorAccessElement(vector_t *vector_ptr, size_t index)
{
	assert(vector_ptr && index < vector_ptr->num_elements);
	
	return (void *)((char *)vector_ptr->arr + index * vector_ptr->element_size);
}

size_t VectorCapacity(const vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	return vector_ptr->num_elements;
}

size_t VectorSize(const vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	return vector_ptr->last_index;
}

int VectorIsEmpty(const vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	return 0 == vector_ptr->last_index;
}

int VectorReserve(vector_t *vector_ptr, size_t num_elements)
{
	void *arr_temp = NULL;
	
	assert(vector_ptr && num_elements);
	
	arr_temp = realloc(vector_ptr->arr, 
						num_elements * vector_ptr->element_size);
	
	if (!arr_temp)
	{
		return FAIL_REALLOC;
	}
	
	if (num_elements < vector_ptr->last_index)
	{
		vector_ptr->last_index = num_elements;
	}
	
	vector_ptr->arr = arr_temp;
	vector_ptr->num_elements = num_elements;
	
	return SUCCESS;
}

int VectorShrinkToFit(vector_t *vector_ptr)
{
	assert(vector_ptr);
	
	return VectorReserve(vector_ptr, vector_ptr->last_index);
}
