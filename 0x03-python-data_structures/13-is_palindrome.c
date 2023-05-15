#include "lists.h"

/**
* reverse_listint - reverses a linked list
* @head: a pointer to the first node in the list
* Return: a pointer to the first node in the new reversed list
*/
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
* is_palindrome - Determines whether a linked list is a palindrome.
* @head: a double pointer to the head of the linked list
*
* Return: return 1 if the linked list is a palindrome,
* 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *current_node = *head;
listint_t *next_node = *head, *list_ptr = *head, *rev_list = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (1)
{
next_node = next_node->next->next;
if (!next_node)
{
rev_list = current_node->next;
break;
}
if (!next_node->next)
{
rev_list = current_node->next->next;
break;
}
current_node = current_node->next;
}

reverse_listint(&rev_list);

while (rev_list && list_ptr)
{
if (list_ptr->n == rev_list->n)
{
rev_list = rev_list->next;
list_ptr = list_ptr->next;
}
else
return (0);
}

if (!rev_list)
return (1);

return (0);
}
