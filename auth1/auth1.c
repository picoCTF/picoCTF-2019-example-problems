#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

static char alphabet[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
				'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
				'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
				'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
				'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
				'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
				'w', 'x', 'y', 'z', '0', '1', '2', '3',
				'4', '5', '6', '7', '8', '9', '+', '/'};

static int mod[] = {0, 2, 1};

char check_password(char *input) {
  int input_length = strlen(input);
  int output_length = 4 * ((input_length + 2) / 3);
  
  char encoded_data[output_length+1];
  
  for (int i = 0, j = 0; i < input_length;) {
    
      unsigned int octet_a = i < input_length ? (unsigned char)input[i++] : 0;
      unsigned int octet_b = i < input_length ? (unsigned char)input[i++] : 0;
      unsigned int octet_c = i < input_length ? (unsigned char)input[i++] : 0;
      
      unsigned int triple = (octet_a << 0x10) + (octet_b << 0x08) + octet_c;
      
      encoded_data[j++] = alphabet[(triple >> 3 * 6) & 0x3F];
      encoded_data[j++] = alphabet[(triple >> 2 * 6) & 0x3F];
      encoded_data[j++] = alphabet[(triple >> 1 * 6) & 0x3F];
      encoded_data[j++] = alphabet[(triple >> 0 * 6) & 0x3F];
  }
  
  for (int i = 0; i < mod[input_length % 3]; i++) {
    encoded_data[output_length - 1 - i] = '=';
  }
  return strncmp(encoded_data, "{{pwd}}", output_length);
}

int main(int argc, char **argv){
  // Set the gid to the effective gid
  //  gid_t gid = getegid();
  //  setresgid(gid, gid, gid);

  setvbuf(stdout, NULL, _IONBF, 0);
  
  if (argc < 2) {
    printf("Please provide a password!\n");
    return -1;
  }

  if (!check_password(argv[1])) {
      printf("Congrats, now where's my flag?\n");
      return 0;
  }
  else {
    printf("Incorrect Password!\n");
    return -1;
  }
}
