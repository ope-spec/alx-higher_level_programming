#include "lists.h"


/**
* is_palindrome - checks if a linked list is a palindrome
* @head: pointer to the head pointer
* Return: 1 for palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *slow = *head, *fast = *head;
while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

listint_t *prev = NULL, *current = slow, *next = NULL;
while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

listint_t *p1 = *head, *p2 = prev;
while (p2)
{
if (p1->n != p2->n)
return (0);
p1 = p1->next;
p2 = p2->next;
}

current = prev, prev = NULL;
while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
slow->next = prev;

return (1);
}
