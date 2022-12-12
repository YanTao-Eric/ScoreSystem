/*
 Navicat Premium Data Transfer

 Source Server         : MySQL@localhost
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : stu_sc_sys

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 12/12/2022 21:54:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes`  (
  `clid` int NOT NULL AUTO_INCREMENT COMMENT '班级id',
  `clyear` int NOT NULL COMMENT '入学年份',
  `clmid` int NOT NULL COMMENT '专业',
  `clno` int NOT NULL COMMENT '班级序号',
  PRIMARY KEY (`clid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES (1, 2020, 1, 1);
INSERT INTO `classes` VALUES (2, 2020, 1, 2);
INSERT INTO `classes` VALUES (3, 2020, 4, 3);
INSERT INTO `classes` VALUES (4, 2020, 5, 4);
INSERT INTO `classes` VALUES (5, 2020, 5, 5);
INSERT INTO `classes` VALUES (6, 2020, 3, 6);
INSERT INTO `classes` VALUES (7, 2020, 2, 7);
INSERT INTO `classes` VALUES (8, 2020, 2, 8);
INSERT INTO `classes` VALUES (9, 2020, 1, 9);
INSERT INTO `classes` VALUES (10, 2020, 2, 10);

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cid` int NOT NULL AUTO_INCREMENT COMMENT '课程代码',
  `cname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '课程名称',
  `cnid` int NOT NULL COMMENT '课程性质',
  `ccredit` float NOT NULL COMMENT '学分',
  `cdid` int NOT NULL COMMENT '开课学院',
  `cmid` int NOT NULL COMMENT '考试方式',
  PRIMARY KEY (`cid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, '大数据程序设计(Python)', 4, 3, 1, 2);
INSERT INTO `course` VALUES (2, '数据结构与算法', 3, 5, 1, 1);
INSERT INTO `course` VALUES (3, '软件工程', 3, 3.5, 1, 1);
INSERT INTO `course` VALUES (4, '计算机网络原理', 3, 3.5, 1, 1);
INSERT INTO `course` VALUES (5, '程序设计基础(网)', 3, 3, 1, 1);
INSERT INTO `course` VALUES (6, 'Linux编程及应用', 4, 3.5, 1, 2);
INSERT INTO `course` VALUES (7, 'WEB前端开发', 4, 2.5, 1, 2);
INSERT INTO `course` VALUES (8, '机械趣味模型', 5, 2, 4, 2);
INSERT INTO `course` VALUES (9, '应用微生物学', 5, 2, 11, 2);
INSERT INTO `course` VALUES (10, '创新性思维与方法', 5, 2, 16, 2);

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `did` int NOT NULL AUTO_INCREMENT COMMENT '学院id',
  `dname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '学院名称',
  PRIMARY KEY (`did`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, '人工智能与大数据学部');
INSERT INTO `department` VALUES (2, '	经济与工商管理学部');
INSERT INTO `department` VALUES (3, '文学与音乐艺术学部');
INSERT INTO `department` VALUES (4, '智能制造学部');
INSERT INTO `department` VALUES (5, '教育学部');
INSERT INTO `department` VALUES (6, '法学与公共管理学部');
INSERT INTO `department` VALUES (7, '国际教育学部');
INSERT INTO `department` VALUES (8, '理学部');
INSERT INTO `department` VALUES (9, '材料与化学工程学部');
INSERT INTO `department` VALUES (10, '艺术与产品设计学部');
INSERT INTO `department` VALUES (11, '农林与食品工程学部');
INSERT INTO `department` VALUES (12, '国际应用技术学部');
INSERT INTO `department` VALUES (13, '质量管理与检验检测学部');
INSERT INTO `department` VALUES (14, '体育与大健康学院');
INSERT INTO `department` VALUES (15, '马克思主义学院');
INSERT INTO `department` VALUES (16, '创新创业学院（继续教育学院）');

-- ----------------------------
-- Table structure for dictionary
-- ----------------------------
DROP TABLE IF EXISTS `dictionary`;
CREATE TABLE `dictionary`  (
  `ddid` int NOT NULL AUTO_INCREMENT COMMENT '数据字典id',
  `ddtype` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '数据字典类型分类',
  `ddtkey` int NOT NULL COMMENT '该分类的主键',
  `ddtvalue` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '该键的值',
  PRIMARY KEY (`ddid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dictionary
-- ----------------------------
INSERT INTO `dictionary` VALUES (1, 'nature', 1, '公共必修课');
INSERT INTO `dictionary` VALUES (2, 'nature', 2, '公共选修课');
INSERT INTO `dictionary` VALUES (3, 'nature', 3, '专业必修课');
INSERT INTO `dictionary` VALUES (4, 'nature', 4, '专业选修课');
INSERT INTO `dictionary` VALUES (5, 'exammethod', 1, '考试');
INSERT INTO `dictionary` VALUES (6, 'exammethod', 2, '考查');
INSERT INTO `dictionary` VALUES (7, 'nature', 5, '通识课');
INSERT INTO `dictionary` VALUES (8, 'majorlevel', 1, '本科');
INSERT INTO `dictionary` VALUES (9, 'majorlevel', 2, '专科');
INSERT INTO `dictionary` VALUES (10, 'role', 1, '学生');
INSERT INTO `dictionary` VALUES (11, 'role', 0, '教师');

-- ----------------------------
-- Table structure for major
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major`  (
  `mid` int NOT NULL AUTO_INCREMENT COMMENT '专业id',
  `mname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '专业名称',
  `mdid` int NOT NULL COMMENT '所属学院',
  `mlid` int NOT NULL DEFAULT 1 COMMENT '教育层次',
  PRIMARY KEY (`mid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES (1, '计算机科学与技术', 1, 1);
INSERT INTO `major` VALUES (2, '软件工程', 1, 1);
INSERT INTO `major` VALUES (3, '数据科学与大数据技术', 1, 1);
INSERT INTO `major` VALUES (4, '信息与计算科学', 1, 1);
INSERT INTO `major` VALUES (5, '数字媒体技术', 1, 1);
INSERT INTO `major` VALUES (6, '物流管理', 2, 1);
INSERT INTO `major` VALUES (7, '工商管理', 2, 1);
INSERT INTO `major` VALUES (8, '财务管理', 2, 1);
INSERT INTO `major` VALUES (9, '国际经济与贸易', 2, 1);
INSERT INTO `major` VALUES (10, '旅游管理', 2, 1);
INSERT INTO `major` VALUES (11, '汉语言文学', 3, 1);
INSERT INTO `major` VALUES (12, '广播电视学', 3, 1);
INSERT INTO `major` VALUES (13, '广播电视编导', 3, 1);
INSERT INTO `major` VALUES (14, '语文教育', 3, 2);
INSERT INTO `major` VALUES (15, '电子信息工程', 4, 1);
INSERT INTO `major` VALUES (16, '机械电子工程', 4, 1);
INSERT INTO `major` VALUES (17, '电子信息科学与技术', 4, 1);
INSERT INTO `major` VALUES (18, '小学教育', 5, 1);
INSERT INTO `major` VALUES (19, '应用心理学', 5, 1);
INSERT INTO `major` VALUES (20, '学前教育', 5, 1);
INSERT INTO `major` VALUES (21, '学前教育', 5, 2);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` int NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `uname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '姓名',
  `ugender` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '男' COMMENT '性别',
  `uidentify` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '身份证号',
  `uclid` int NOT NULL COMMENT '班级',
  `uemail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `upwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `urole` int NOT NULL DEFAULT 1 COMMENT '用户的角色',
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 220003 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (200001, 'Alice', '女', '513721200111111234', 9, 'alice123@foxmail.com', '123456', 1);
INSERT INTO `user` VALUES (200002, 'Jobs', '男', NULL, 1, NULL, '123456', 1);
INSERT INTO `user` VALUES (220001, 'Eric', '男', '513721200110272736', 9, '2810950897@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220002, 'Steve', '男', '123456789012345678', 9, '471404371@qq.com', '123456', 0);

-- ----------------------------
-- Table structure for user_course
-- ----------------------------
DROP TABLE IF EXISTS `user_course`;
CREATE TABLE `user_course`  (
  `ucid` int NOT NULL AUTO_INCREMENT COMMENT '学生-课程id',
  `uid` int NOT NULL,
  `cid` int NOT NULL,
  `score` decimal(6, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`ucid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_course
-- ----------------------------
INSERT INTO `user_course` VALUES (1, 200001, 1, NULL);
INSERT INTO `user_course` VALUES (2, 200001, 2, NULL);
INSERT INTO `user_course` VALUES (3, 200001, 3, NULL);
INSERT INTO `user_course` VALUES (4, 200001, 4, NULL);
INSERT INTO `user_course` VALUES (5, 200001, 5, NULL);
INSERT INTO `user_course` VALUES (6, 200001, 6, NULL);
INSERT INTO `user_course` VALUES (7, 200001, 7, NULL);
INSERT INTO `user_course` VALUES (8, 200001, 8, NULL);
INSERT INTO `user_course` VALUES (9, 200001, 9, NULL);
INSERT INTO `user_course` VALUES (10, 200001, 10, NULL);
INSERT INTO `user_course` VALUES (11, 200002, 1, NULL);
INSERT INTO `user_course` VALUES (12, 200002, 2, NULL);
INSERT INTO `user_course` VALUES (13, 200002, 3, NULL);
INSERT INTO `user_course` VALUES (14, 200002, 4, NULL);
INSERT INTO `user_course` VALUES (15, 200002, 5, NULL);
INSERT INTO `user_course` VALUES (16, 200002, 6, NULL);
INSERT INTO `user_course` VALUES (17, 200002, 7, NULL);
INSERT INTO `user_course` VALUES (18, 200002, 8, NULL);
INSERT INTO `user_course` VALUES (19, 200002, 9, NULL);
INSERT INTO `user_course` VALUES (20, 200002, 10, NULL);

SET FOREIGN_KEY_CHECKS = 1;
