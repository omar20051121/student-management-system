#include <stdio.h>

int get_digit_sum(long long credit);
int get_credit_length(long long credit);
const char* get_card_type(long long credit);

int main(void)
{
    long long number;

    printf("Number: ");
    if (scanf("%lld", &number) != 1) {
        printf("INVALID\n");
        return 0;
    }

    // Check valid length
    int length = get_credit_length(number);
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Check Luhn's algorithm
    int sum = get_digit_sum(number);
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Determine card type
    const char* type = get_card_type(number);
    printf("%s\n", type);
    return 0;
}

// Returns the length of the credit number
int get_credit_length(long long credit)
{
    int length = 0;
    while (credit > 0)
    {
        credit /= 10;
        length++;
    }
    return length;
}

// Returns the sum of digits according to Luhn's algorithm
int get_digit_sum(long long credit)
{
    int sum = 0;
    int is_second = 0;

    while (credit > 0)
    {
        int digit = credit % 10;
        if (is_second)
        {
            int product = digit * 2;
            sum += (product / 10) + (product % 10); // sum digits of product
        }
        else
        {
            sum += digit;
        }
        is_second = !is_second;
        credit /= 10;
    }

    return sum;
}

// Determines card type based on starting digits
const char* get_card_type(long long credit)
{
    int length = get_credit_length(credit);
    long long start = credit;
    while (start >= 100)
    {
        start /= 10; // reduce to first 1 or 2 digits
    }

    int first_digit = start / 10;
    int first_two = start;

    if ((length == 13 || length == 16) && first_digit == 4)
    {
        return "VISA";
    }
    else if (length == 15 && (first_two == 34 || first_two == 37))
    {
        return "AMEX";
    }
    else if (length == 16 && (first_two >= 51 && first_two <= 55))
    {
        return "MASTERCARD";
    }
    else
    {
        return "INVALID";
    }
}
