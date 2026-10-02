import mujoco
import mujoco.viewer


MODEL = "models/templates/world.xml"


def main():

    model = mujoco.MjModel.from_xml_path(MODEL)

    data = mujoco.MjData(model)

    with mujoco.viewer.launch_passive(model, data) as viewer:

        while viewer.is_running():

            mujoco.mj_step(model, data)

            viewer.sync()


if __name__ == "__main__":

    main()