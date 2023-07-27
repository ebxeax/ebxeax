#include <iostream>
#define dtype unsigned int 

class TLB
{
private:
    dtype idx;
    dtype *data;
    dtype block_idx;

public:
    void set_idx(unsigned id){}
    dtype get_block_idx() { return block_idx; }
    dtype get_data(int id) { return data[id]; }
};

class sTLB : TLB
{
private:
    dtype tag = 0;
    dtype cache = 0;
public :
    void set_tag(dtype t){ tag = t; }
    void set_cache(dtype c){ cache = c; }
    void print_info() { std::cout << tag << " " << cache << std::endl; }
};
