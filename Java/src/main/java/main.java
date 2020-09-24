import adaptation_planner_layer.ManagingSystem;

public class main {
    public static void main(String[] args){
        ManagingSystem managingSys = new ManagingSystem();


        //while (true) {
        int i = 0;
        while (i < 10) {
            managingSys.adaptManagedSystem();
            i++;
        }
    }
}
