#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/saisriteja/htic_spine_surgery_robotics/src/universal_robot/ur_kinematics"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/saisriteja/htic_spine_surgery_robotics/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/saisriteja/htic_spine_surgery_robotics/install/lib/python2.7/dist-packages:/home/saisriteja/htic_spine_surgery_robotics/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/saisriteja/htic_spine_surgery_robotics/build" \
    "/usr/bin/python2" \
    "/home/saisriteja/htic_spine_surgery_robotics/src/universal_robot/ur_kinematics/setup.py" \
     \
    build --build-base "/home/saisriteja/htic_spine_surgery_robotics/build/universal_robot/ur_kinematics" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/saisriteja/htic_spine_surgery_robotics/install" --install-scripts="/home/saisriteja/htic_spine_surgery_robotics/install/bin"
