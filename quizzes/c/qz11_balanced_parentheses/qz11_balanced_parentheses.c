#include "stack.h"
#include <string.h> /* strlen */
#include <assert.h> /* assert */
#include <stdio.h>	/* printf */

const char brackets_lut[] = {'{', '}', '[', ']', '(', ')'};
const unsigned int size = sizeof(brackets_lut) / sizeof(brackets_lut[0]);

int GetBracketIndex(char ch)
{
	unsigned int i = 0;

	for (; i < size; i++)
	{
		if (ch == brackets_lut[i])
		{
			return i;
		}
	}

	return -1;
}

int IsBalancedBrackets(const char *str)
{
	int res = 0;
	int lut_index = 0;
	stack_t *stck = NULL;

	assert(str);

	stck = StackCreate(strlen(str));

	if (!stck)
	{
		return -1;
	}

	for (; *str; str++)
	{
		lut_index = GetBracketIndex(*str);

		if (-1 == lut_index)
		{
			continue;
		}

		if (lut_index & 1)
		{
			if (!StackIsEmpty(stck) && brackets_lut[lut_index - 1] == *(char *)StackPeek(stck))
			{
				StackPop(stck);
			}
			else
			{
				return 0;
			}
		}
		else
		{
			StackPush(stck, (void *)str);
		}
	}

	res = StackIsEmpty(stck);

	StackDestroy(stck);
	stck = NULL;

	return res;
}

int main()
{
	printf("%d\n", IsBalancedBrackets("]"));
	printf("%d\n", IsBalancedBrackets("{"));
	printf("%d\n", IsBalancedBrackets("g))^;{}df"));
	printf("%d\n", IsBalancedBrackets("f(dsa)f()){}[]"));

	printf("%d\n", IsBalancedBrackets("({[]})"));
	printf("%d\n", IsBalancedBrackets("({f}s)[]"));
	printf("%d\n", IsBalancedBrackets("(x)({}bf[])"));

	return 0;
}
