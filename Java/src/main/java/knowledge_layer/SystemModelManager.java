package knowledge_layer;
import specification.*;

public class SystemModelManager {
    public SystemModel sysModel;

    public SystemModelManager(SystemModel sys){
        sysModel = sys;
    }

    public void updateModel(){
        //todo: specify how to update model
        sysModel.setModel();
    }

    public SystemModel getSysModel(){
        return sysModel;
    }
}
