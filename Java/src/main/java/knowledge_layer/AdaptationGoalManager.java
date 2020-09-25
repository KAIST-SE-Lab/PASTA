package knowledge_layer;

import specification.AdaptationGoal;

public class AdaptationGoalManager {
    private AdaptationGoal goal;

    public AdaptationGoalManager(AdaptationGoal adaptationGoal) {
        goal = adaptationGoal;
    }

    public AdaptationGoal getGoal() {
        return goal;
    }

    public void setGoal(AdaptationGoal newGoal) {
        goal = newGoal;

    }
}
