#include "simTLB.h"

int main()
{   
    unsigned int cache, tag;
    cache = 10;
    tag = 20;
    sTLB stlb;
    stlb.set_cache(cache);
    stlb.set_tag(tag);
    stlb.print_info();
    return 0;
}