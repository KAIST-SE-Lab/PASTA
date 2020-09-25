package knowledge_layer;

import specification.SystemModel;

public class SystemModelManager {
    public SystemModel sysModel;

    public SystemModelManager(SystemModel sys) {
        sysModel = sys;
    }

    public void updateModel() {
        //todo: specify how to update model
    }

    public SystemModel getSysModel() {
        return sysModel;
    }
}
