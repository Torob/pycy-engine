#pragma once
#include <cctype>
#include <iostream>
#include <cstring>
#include <cstdio>

class TestModule {
    
    public:
        void initiate() {
            std::cout << "Starting to initiate";
            // do some time consuming work
        }

        std::string get_answer(std::string query) {
            char * ans = new char[query.length()];
            for(int i=0; i<query.length(); i++) {
                ans += toupper(query[i]);
            }
            return ans;
        }
};