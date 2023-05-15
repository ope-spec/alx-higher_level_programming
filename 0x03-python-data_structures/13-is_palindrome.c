#include "lists.h"


/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to the head of the list
*
* Return: 0 if not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
listint_t *temp = *head;
int stack[1024], top = -1;

while (current != NULL)
{
stack[++top] = current->n;
current = current->next;
}

while (temp != NULL)
{
if (temp->n != stack[top--])
return (0);
temp = temp->next;
}
return (1);
}
