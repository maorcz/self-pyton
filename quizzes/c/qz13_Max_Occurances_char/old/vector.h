#ifndef __OL113_VECTOR_H__
#define __OL113_VECTOR_H__

#include <stddef.h> /* size_t */

/*****************************************************************************
 * version 2.0 BLUE TEAM                                                     *
 *****************************************************************************/

typedef struct dynamic_vector vector_t;

/* num_elements must be greater than 0, size_element must be greater than 0 */
vector_t *VectorCreate(size_t num_elements, size_t element_size);
void VectorDestroy(vector_t *vector);

/* pop from empty vector is undefined */
void VectorPopBack(vector_t *vector);
int VectorPushBack(vector_t *vector, const void *val);
/*  index must be smaller than size, pointer return is temporary, and might void after further pushbacks  */
void *VectorAccessElement(vector_t *vector, size_t index);

size_t VectorCapacity(const vector_t *vector);
size_t VectorSize(const vector_t *vector);
int VectorIsEmpty(const vector_t *vector);
/*  num_element must be greater than 0 */
int VectorReserve(vector_t *vector, size_t num_elements);
int VectorShrinkToFit(vector_t *vector);

#endif /* __OL113_DYNAMIC_VECTOR_H__ */


