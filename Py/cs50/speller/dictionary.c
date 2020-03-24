// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
int count = 0;
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = NULL;
        new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        strcpy(new_node->word, word);
        int bucketIndex = hash(new_node->word);
        new_node->next = NULL;
        if (hashtable[bucketIndex] == NULL)
        {
            hashtable[bucketIndex] = new_node;
        }
        else
        {
            new_node->next = hashtable[bucketIndex];
            hashtable[bucketIndex] = new_node;
        }
        count++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (&load)
    {
        return count;
    }
    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int textHash = hash(word);
    int comparison = 0;
    node *cursor = hashtable[textHash];
    while (cursor != NULL)
    {
        comparison = strcasecmp(cursor->word, word);
        cursor = cursor->next;
        if (comparison == 0)
        {
            return true;
        }
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];

        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}