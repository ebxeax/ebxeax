#include "simTLB.h"

int main()
{   
    dtype cache, tag;
    cache = 10;
    tag = 20;
    sTLB stlb;
    stlb.set_cache(cache);
    stlb.set_tag(tag);
    stlb.print_info();
    TLB tlb;
    tlb.set_idx(tag);
    return 0;
}