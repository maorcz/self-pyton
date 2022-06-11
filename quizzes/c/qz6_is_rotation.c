#include <stdio.h>
#include <string.h>
#include <assert.h>

int IsRotation(const char *str1, const char *str2);
void Test(void);
void PrintSuccessOrFail(int is_worked);

int main()
{
	Test();
	
	return 0;
}

int IsRotation(const char *str1, const char *str2)
{
	size_t len = 0;
	size_t i = 0;
	
	assert(str1 || str2);
	
	len = strlen(str1);
	
	if (len != strlen(str2))
	{
		return 0;
	}
	
	for ( ; i < len ; i++)
	{
		if (str1[0] == str2[i])
		{
			if (!strncmp(str1, str2 + i, len - i))
			{
			 	if (!strncmp(str1 +	(len-i), str2, i))
			 	{
			 		return 1;
				}
			}
		}
	}
	
	return 0;
}

void Test(void)
{
	PrintSuccessOrFail(1 == IsRotation("ffg", "fgf"));
	PrintSuccessOrFail(1 == IsRotation("gff", "fgf"));
	PrintSuccessOrFail(1 == IsRotation("fgf", "gff"));
	PrintSuccessOrFail(1 == IsRotation("a1a12345", "1a12345a"));
	PrintSuccessOrFail(1 == IsRotation("ehheh", "hehhe"));
	PrintSuccessOrFail(1 == IsRotation("112121", "212111"));
	PrintSuccessOrFail(1 == IsRotation("aab1aaa", "aaab1aa"));
	PrintSuccessOrFail(1 == IsRotation("12345", "45123"));
	PrintSuccessOrFail(1 == IsRotation("121234", "123412"));
}

void PrintSuccessOrFail(int is_worked)
{
	printf("%s\n", is_worked ? "Succeeded" : "Failed");
}
