package knowledge_layer;
import specification.*;
import java.util.ArrayList;

public class AdaptationGoalManager {
    private AdaptationGoal goal;

    public AdaptationGoalManager(AdaptationGoal adaptationGoal){
        goal = adaptationGoal;
    }

    public void setGoal(AdaptationGoal newGoal){
        goal = newGoal;

    }
    public AdaptationGoal getGoal(){
        return goal;
    }
}
