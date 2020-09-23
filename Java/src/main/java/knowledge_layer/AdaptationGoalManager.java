package knowledge_layer;
import specification.*;
import java.util.ArrayList;

public class AdaptationGoalManager {
    public AdaptationGoal goal;

    public AdaptationGoalManager(AdaptationGoal adaptationGoal){
        goal = adaptationGoal;
    }

    public AdaptationGoal getGoal(){
        return goal;
    }
}
