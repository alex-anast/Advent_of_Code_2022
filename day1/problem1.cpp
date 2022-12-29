#include <iostream>
#include <fstream>

int main(void){
    std::fstream my_file;
    my_file.open("data_input", std::ios::in);

    if (!my_file){
        std::cout << "Problem reading the file!" << std::endl;
    }
    else {
        char ch;
        while (1){
            my_file >> ch;
            if (my_file.eof()){
                break;
            }
            std::cout << ch;
        }
    }

    my_file.close();
    return 0;
}
