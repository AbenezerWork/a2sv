class Robot {
    int width,height;
    int stp=0;
    int total=0;
    int mod;
public:
    Robot(int width, int height) {
        this->width = width;
        this->height = height;
        this->mod = 2*height +2*width - 4;
    }
    
    void step(int num) {
        stp=(stp+num)%mod;
        total+=num;
        cout<<stp<<endl;
    }
    
    vector<int> getPos() {
        vector<int> pos(2);
        if(stp<width-1){
            pos[0]=stp;
            pos[1]=0;
        }else if(stp<(width+height-1)){
            pos[0]=width-1;
            pos[1]=stp-(width)+1;
        }else if(stp<(2*width+height-2)){
            pos[0]=width-(stp - (width+height-2))-1;
            pos[1]=height-1;
        }else{
            pos[0]=0;
            pos[1]=height-(stp-(2*width+height-3))-1;
        }
        return pos;
    }
    
    string getDir() {

        string d[]={"East","North","West","South"};
        if(total==0){
            return "East";
        }else if (stp == 0){
            return "South";
        }else if(stp<=width-1){
            //cout<<"--"<<stp<<endl;
            return "East";
        }else if(stp<(width+height-1)){
            return "North";
        }else if(stp<(2*width+height-2)){
            return "West";
        }else{
            return "South";
        }
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */