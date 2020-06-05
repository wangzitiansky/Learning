#include <iostream>
#include <cstring>

const int N = 110;
int e[N], ne[N], h[N];
int idx;
int q[N];
int d[N];
int n, m;


void add(int a, int b){
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx ++;
}

void top_sort(){
    int hh =0, tt = -1;

    for(int i = 1; i <= n; i ++){
        if(!d[i]){
            q[++ tt] = i;
        }
    }

    while(hh <= tt){
        int t = q[hh ++];
        for(int i = h[t]; i != -1; i = ne[i]){
            int j = e[i];
            if(-- d[j] == 0){
                q[++ tt] = j;
            }
        }
    }

}

int main(int argc, char const *argv[])
{
    

    while(scanf("%d %d", &n, &m)){
        if(m == 0 && n == 0) break;
        if(m == 0){
            for (int i = 1; i <= n; i++)
            {
                printf("%d ", i);
            }
            puts("");
        } else {

            memset(h, -1, sizeof(h));
            memset(ne, 0, sizeof(ne));
            memset(e, 0, sizeof(e));
            memset(q, 0, sizeof(q));
            memset(d, 0, sizeof(d));
            idx = 0;
            while(m --){
                int a,  b;
                scanf("%d %d", &a, &b);
                add(a, b);
                d[b] ++;
            }
            top_sort();

            for(int i = 0; i < n; i ++){
                printf("%d ", q[i]);
            }

            puts("");
        }
    }

    
}
