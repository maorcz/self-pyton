#include <stdio.h>

void PrintMove(int n, char from, char to)
{
	printf("move Disk %d from rod %c to rod %c\n", n, from, to);
}

void TowerOfHanoi(int n, char from, char to, char aux)
{
	if (n == 1)
	{
		PrintMove(n, from, to);

		return;
	}

	TowerOfHanoi(n - 1, from, aux, to);
	PrintMove(n, from, to);
	TowerOfHanoi(n - 1, aux, to, from);
}

int main()
{
	TowerOfHanoi(4, 'A', 'B', 'C');

	return 0;
}