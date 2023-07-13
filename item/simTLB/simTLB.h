#include <iostream>

class TLB
{
private:
    int idx;
    int *data;
    int block_idx;

public:
    int get_block_idx() { return block_idx; }
    int get_data(int id) { return data[id]; }
};

class sTLB : TLB
{
private:
    unsigned int tag = 0;
    unsigned int cache = 0;
public :
    void set_tag(unsigned int t){ tag = t; }
    void set_cache(unsigned int c){ cache = c; }
    void print_info() { std::cout << tag << " " << cache << std::endl; }
};
