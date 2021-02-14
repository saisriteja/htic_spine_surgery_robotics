// Generated by gencpp from file ur_msgs/RobotModeDataMsg.msg
// DO NOT EDIT!


#ifndef UR_MSGS_MESSAGE_ROBOTMODEDATAMSG_H
#define UR_MSGS_MESSAGE_ROBOTMODEDATAMSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ur_msgs
{
template <class ContainerAllocator>
struct RobotModeDataMsg_
{
  typedef RobotModeDataMsg_<ContainerAllocator> Type;

  RobotModeDataMsg_()
    : timestamp(0)
    , is_robot_connected(false)
    , is_real_robot_enabled(false)
    , is_power_on_robot(false)
    , is_emergency_stopped(false)
    , is_protective_stopped(false)
    , is_program_running(false)
    , is_program_paused(false)  {
    }
  RobotModeDataMsg_(const ContainerAllocator& _alloc)
    : timestamp(0)
    , is_robot_connected(false)
    , is_real_robot_enabled(false)
    , is_power_on_robot(false)
    , is_emergency_stopped(false)
    , is_protective_stopped(false)
    , is_program_running(false)
    , is_program_paused(false)  {
  (void)_alloc;
    }



   typedef uint64_t _timestamp_type;
  _timestamp_type timestamp;

   typedef uint8_t _is_robot_connected_type;
  _is_robot_connected_type is_robot_connected;

   typedef uint8_t _is_real_robot_enabled_type;
  _is_real_robot_enabled_type is_real_robot_enabled;

   typedef uint8_t _is_power_on_robot_type;
  _is_power_on_robot_type is_power_on_robot;

   typedef uint8_t _is_emergency_stopped_type;
  _is_emergency_stopped_type is_emergency_stopped;

   typedef uint8_t _is_protective_stopped_type;
  _is_protective_stopped_type is_protective_stopped;

   typedef uint8_t _is_program_running_type;
  _is_program_running_type is_program_running;

   typedef uint8_t _is_program_paused_type;
  _is_program_paused_type is_program_paused;





  typedef boost::shared_ptr< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> const> ConstPtr;

}; // struct RobotModeDataMsg_

typedef ::ur_msgs::RobotModeDataMsg_<std::allocator<void> > RobotModeDataMsg;

typedef boost::shared_ptr< ::ur_msgs::RobotModeDataMsg > RobotModeDataMsgPtr;
typedef boost::shared_ptr< ::ur_msgs::RobotModeDataMsg const> RobotModeDataMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ur_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ur_msgs': ['/home/saisriteja/htic_spine_surgery_robotics/src/universal_robot/ur_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "867308ca39e2cc0644b50db27deb661f";
  }

  static const char* value(const ::ur_msgs::RobotModeDataMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x867308ca39e2cc06ULL;
  static const uint64_t static_value2 = 0x44b50db27deb661fULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_msgs/RobotModeDataMsg";
  }

  static const char* value(const ::ur_msgs::RobotModeDataMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This data structure contains the RobotModeData structure\n\
# used by the Universal Robots controller\n\
#\n\
# This data structure is send at 10 Hz on TCP port 30002\n\
#\n\
# Note: this message does not carry all fields from the RobotModeData structure as broadcast by the robot controller, but a subset.\n\
\n\
uint64 timestamp\n\
bool is_robot_connected\n\
bool is_real_robot_enabled\n\
bool is_power_on_robot\n\
bool is_emergency_stopped\n\
bool is_protective_stopped\n\
bool is_program_running\n\
bool is_program_paused\n\
";
  }

  static const char* value(const ::ur_msgs::RobotModeDataMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.timestamp);
      stream.next(m.is_robot_connected);
      stream.next(m.is_real_robot_enabled);
      stream.next(m.is_power_on_robot);
      stream.next(m.is_emergency_stopped);
      stream.next(m.is_protective_stopped);
      stream.next(m.is_program_running);
      stream.next(m.is_program_paused);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RobotModeDataMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_msgs::RobotModeDataMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_msgs::RobotModeDataMsg_<ContainerAllocator>& v)
  {
    s << indent << "timestamp: ";
    Printer<uint64_t>::stream(s, indent + "  ", v.timestamp);
    s << indent << "is_robot_connected: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_robot_connected);
    s << indent << "is_real_robot_enabled: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_real_robot_enabled);
    s << indent << "is_power_on_robot: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_power_on_robot);
    s << indent << "is_emergency_stopped: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_emergency_stopped);
    s << indent << "is_protective_stopped: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_protective_stopped);
    s << indent << "is_program_running: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_program_running);
    s << indent << "is_program_paused: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_program_paused);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_MSGS_MESSAGE_ROBOTMODEDATAMSG_H
