#include "stack.h"
#include <string.h> /* strlen */
#include <stdio.h> /* printf */

int IsBalancedBrackets(const char *str)
{
	int is_pushed = 0;
	int ans = 0;
	stack_t *stck = StackCreate(strlen(str));
	char char_to_pop = '\0';
	
	if (!stck)
	{
		return -1;
	}
	
	for ( ; *str ; str++)
	{
		char_to_pop = GetOpenBracketFromClose(*str);
		
		if (char_to_pop && is_pushed)
		{
			if (char_to_pop == *(char *)StackPeek(stck))
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
			StackPush(stck, str);
			is_pushed = 1;
		}
	}
	
	ans = StackIsEmpty(stck);
	
	StackDestroy(stck);
	stck = NULL;
	
	return ans;
}


int main()
{
	printf("%d\n", IsBalancedBrackets("(){}[]"));
	printf("%d\n", IsBalancedBrackets("({})[]"));
	printf("%d\n", IsBalancedBrackets("({}[)]"));
	
	return 0;
}


