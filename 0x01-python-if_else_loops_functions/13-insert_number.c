#include "lists.h"

/**
* insert_node - adds a number to a sorted singly linked list.
* @head: pointer to the linked list's head.
* @number: Number to insert into the linked list.
*
* Return: Address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node_ptr = malloc(sizeof(listint_t));

if (node_ptr == NULL)
{
return (NULL);
}

node_ptr->n = number;
node_ptr->next = NULL;

if (*head == NULL || (*head)->n >= number)
{
node_ptr->next = *head;
*head = node_ptr;
}
else
{
listint_t *current = *head;

while (current->next != NULL && current->next->n < number)
{
current = current->next;
}

node_ptr->next = current->next;
current->next = node_ptr;
}

return (node_ptr);
}
