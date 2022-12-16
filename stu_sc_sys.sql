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

 Date: 16/12/2022 15:02:05
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
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
  `cnature` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '课程性质',
  `ccredit` decimal(3, 1) NOT NULL COMMENT '学分',
  `cdepartment` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '开课学院',
  `cexammethod` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '考试方式',
  PRIMARY KEY (`cid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, '大数据程序设计(Python)', '专业选修课', 3.0, '人工智能与大数据学部', '考查');
INSERT INTO `course` VALUES (2, '数据结构与算法', '专业必修课', 5.0, '人工智能与大数据学部', '考试');
INSERT INTO `course` VALUES (3, '软件工程', '专业必修课', 3.5, '人工智能与大数据学部', '考试');
INSERT INTO `course` VALUES (4, '计算机网络原理', '专业必修课', 3.5, '人工智能与大数据学部', '考试');
INSERT INTO `course` VALUES (5, '程序设计基础(网)', '专业必修课', 3.0, '人工智能与大数据学部', '考试');
INSERT INTO `course` VALUES (6, 'Linux编程及应用', '专业选修课', 3.5, '人工智能与大数据学部', '考查');
INSERT INTO `course` VALUES (7, 'WEB前端开发', '专业选修课', 2.5, '人工智能与大数据学部', '考查');
INSERT INTO `course` VALUES (8, '机械趣味模型', '通识课', 2.0, '智能制造学部', '考查');
INSERT INTO `course` VALUES (9, '应用微生物学', '通识课', 2.0, '农林与食品工程学部', '考查');
INSERT INTO `course` VALUES (10, '创新性思维与方法', '通识课', 2.0, '创新创业学院（继续教育学院）', '考查');
INSERT INTO `course` VALUES (11, 'Java课程设计', '专业必修课', 4.0, '人工智能与大数据学部', '考试');
INSERT INTO `course` VALUES (19, 'JavaEE企业开发', '专业选修课', 4.0, '人工智能与大数据学部', '考查');

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `did` int NOT NULL AUTO_INCREMENT COMMENT '学院id',
  `dname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '学院名称',
  PRIMARY KEY (`did`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, '人工智能与大数据学部');
INSERT INTO `department` VALUES (2, '经济与工商管理学部');
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
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
  `uclid` int NULL DEFAULT NULL COMMENT '班级',
  `uemail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `upwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `urole` int NOT NULL DEFAULT 1 COMMENT '用户的角色',
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 220004 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (8888, '严涛', '男', '513721200110272736', 0, '2810950897@qq.com', 'admin', 0);
INSERT INTO `user` VALUES (200001, 'Amy', '女', '511921200206102159', 9, 'amy123@foxmail.com', 'amy123456', 1);
INSERT INTO `user` VALUES (200002, 'Jobs', '男', '511920199808301459', 1, 'jobs@apple.com', '123456', 1);
INSERT INTO `user` VALUES (220001, 'Eric', '男', '511920199808301459', 9, '2810950897@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220002, 'Steve', '男', '511920199808301459', 9, '471404371@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220003, '张三', '男', '123456789', 9, '1234567890@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220004, '李四', '男', '511921200206102159', 9, '2810950897@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220005, '肖婷', '女', '511921200206102159', 9, '3805088127@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220006, '李彦斌', '男', '511921200206102159', 9, '5221836178@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220007, '吴青峰', '男', '511921200206102159', 9, '7380192637@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220008, '李薇', '女', '511921200206102159', 9, '1762882394@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220009, '薛晓', '女', '511921200206102159', 9, '3210685219@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220010, '张子枫', '女', '511921200206102159', 9, '6582105978@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220011, '李治廷', '男', '511921200206102159', 9, '2747925856@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220012, '柏平', '男', '511921200206102159', 9, '4862031982@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220013, '刘婷', '女', '511921200206102159', 9, '1038742968@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220014, '章泽天', '女', '511921200206102159', 9, '1325794031@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220015, '李晨', '男', '511921200206102159', 9, '5231520987@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220016, '周洁琼', '女', '511921200206102159', 9, '1352013875@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220017, '杨开慧', '女', '511921200206102159', 9, '6213475698@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220018, '张强', '男', '511921200206102159', 9, '3207413852@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220019, '王阳明', '男', '511921200206102159', 9, '3152013875@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220020, '杨明', '男', '511921200206102159', 9, '4851302965@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220021, '高静', '女', '511921200206102159', 9, '9531027459@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220022, '冯鑫', '男', '511921200206102159', 9, '5137452039@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220023, '陆萍', '女', '511921200206102159', 9, '3207461826@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220024, '李宁', '男', '511921200206102159', 9, '6874310594@qq.com', '123456', 1);
INSERT INTO `user` VALUES (220025, '李俊英', '女', '511921200206102159', 9, '3107840689@qq.com', '123456', 1);

-- ----------------------------
-- Table structure for user_course
-- ----------------------------
DROP TABLE IF EXISTS `user_course`;
CREATE TABLE `user_course`  (
  `ucid` int NOT NULL AUTO_INCREMENT COMMENT '学生-课程id',
  `uid` int NOT NULL COMMENT '学号',
  `cname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '课程名',
  `score` decimal(6, 2) NULL DEFAULT NULL COMMENT '成绩',
  PRIMARY KEY (`ucid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_course
-- ----------------------------
INSERT INTO `user_course` VALUES (1, 200001, '大数据程序设计(Python)', 91.00);
INSERT INTO `user_course` VALUES (2, 200001, '数据结构与算法', 82.00);
INSERT INTO `user_course` VALUES (3, 200001, '软件工程', 73.50);
INSERT INTO `user_course` VALUES (4, 200001, '计算机网络原理', 88.00);
INSERT INTO `user_course` VALUES (5, 200001, '程序设计基础(网)', 62.00);
INSERT INTO `user_course` VALUES (6, 200001, 'Linux编程及应用', 87.00);
INSERT INTO `user_course` VALUES (7, 200001, 'WEB前端开发', 76.00);
INSERT INTO `user_course` VALUES (8, 200001, '机械趣味模型', 81.00);
INSERT INTO `user_course` VALUES (9, 200001, '应用微生物学', 38.00);
INSERT INTO `user_course` VALUES (10, 200001, '创新性思维与方法', 86.00);
INSERT INTO `user_course` VALUES (11, 200002, '大数据程序设计(Python)', 91.00);
INSERT INTO `user_course` VALUES (12, 200002, '数据结构与算法', 66.00);
INSERT INTO `user_course` VALUES (13, 200002, '软件工程', 77.00);
INSERT INTO `user_course` VALUES (14, 200002, '计算机网络原理', 86.00);
INSERT INTO `user_course` VALUES (15, 200002, '程序设计基础(网)', 85.50);
INSERT INTO `user_course` VALUES (16, 200002, 'Linux编程及应用', 81.50);
INSERT INTO `user_course` VALUES (17, 200002, 'WEB前端开发', 80.00);
INSERT INTO `user_course` VALUES (18, 200002, '机械趣味模型', 71.00);
INSERT INTO `user_course` VALUES (19, 200002, '应用微生物学', 68.50);
INSERT INTO `user_course` VALUES (20, 200002, '创新性思维与方法', 73.00);
INSERT INTO `user_course` VALUES (21, 220003, '大数据程序设计(Python)', 95.00);
INSERT INTO `user_course` VALUES (22, 220003, '数据结构与算法', 91.00);
INSERT INTO `user_course` VALUES (23, 220003, '软件工程', 99.00);
INSERT INTO `user_course` VALUES (24, 220003, '计算机网络原理', 70.00);
INSERT INTO `user_course` VALUES (25, 220003, '程序设计基础(网)', 62.00);
INSERT INTO `user_course` VALUES (26, 220003, 'Linux编程及应用', 52.00);
INSERT INTO `user_course` VALUES (27, 220003, 'WEB前端开发', 63.00);
INSERT INTO `user_course` VALUES (28, 220003, '机械趣味模型', 87.00);
INSERT INTO `user_course` VALUES (29, 220003, '应用微生物学', 72.00);
INSERT INTO `user_course` VALUES (30, 220003, '创新性思维与方法', 79.00);
INSERT INTO `user_course` VALUES (31, 220003, 'Java课程设计', 57.00);
INSERT INTO `user_course` VALUES (32, 220003, 'JavaEE企业开发', 53.00);
INSERT INTO `user_course` VALUES (33, 220004, '大数据程序设计(Python)', 97.00);
INSERT INTO `user_course` VALUES (34, 220004, '数据结构与算法', 96.00);
INSERT INTO `user_course` VALUES (35, 220004, '软件工程', 88.00);
INSERT INTO `user_course` VALUES (36, 220004, '计算机网络原理', 93.00);
INSERT INTO `user_course` VALUES (37, 220004, '程序设计基础(网)', 56.00);
INSERT INTO `user_course` VALUES (38, 220004, 'Linux编程及应用', 89.00);
INSERT INTO `user_course` VALUES (39, 220004, 'WEB前端开发', 97.00);
INSERT INTO `user_course` VALUES (40, 220004, '机械趣味模型', 96.00);
INSERT INTO `user_course` VALUES (41, 220004, '应用微生物学', 97.50);
INSERT INTO `user_course` VALUES (42, 220004, '创新性思维与方法', 94.00);
INSERT INTO `user_course` VALUES (43, 220004, 'Java课程设计', 92.00);
INSERT INTO `user_course` VALUES (44, 220004, 'JavaEE企业开发', 94.00);
INSERT INTO `user_course` VALUES (45, 220005, '大数据程序设计(Python)', 95.00);
INSERT INTO `user_course` VALUES (46, 220005, '数据结构与算法', 63.00);
INSERT INTO `user_course` VALUES (47, 220005, '软件工程', 70.00);
INSERT INTO `user_course` VALUES (48, 220005, '计算机网络原理', 92.00);
INSERT INTO `user_course` VALUES (49, 220005, '程序设计基础(网)', 65.00);
INSERT INTO `user_course` VALUES (50, 220005, 'Linux编程及应用', 100.00);
INSERT INTO `user_course` VALUES (51, 220005, 'WEB前端开发', 53.00);
INSERT INTO `user_course` VALUES (52, 220005, '机械趣味模型', 53.00);
INSERT INTO `user_course` VALUES (53, 220005, '应用微生物学', 84.00);
INSERT INTO `user_course` VALUES (54, 220005, '创新性思维与方法', 69.00);
INSERT INTO `user_course` VALUES (55, 220005, 'Java课程设计', 98.00);
INSERT INTO `user_course` VALUES (56, 220005, 'JavaEE企业开发', 67.00);
INSERT INTO `user_course` VALUES (57, 220006, '大数据程序设计(Python)', 91.00);
INSERT INTO `user_course` VALUES (58, 220006, '数据结构与算法', 51.00);
INSERT INTO `user_course` VALUES (59, 220006, '软件工程', 58.00);
INSERT INTO `user_course` VALUES (60, 220006, '计算机网络原理', 54.00);
INSERT INTO `user_course` VALUES (61, 220006, '程序设计基础(网)', 57.00);
INSERT INTO `user_course` VALUES (62, 220006, 'Linux编程及应用', 77.00);
INSERT INTO `user_course` VALUES (63, 220006, 'WEB前端开发', 87.00);
INSERT INTO `user_course` VALUES (64, 220006, '机械趣味模型', 92.00);
INSERT INTO `user_course` VALUES (65, 220006, '应用微生物学', 68.00);
INSERT INTO `user_course` VALUES (66, 220006, '创新性思维与方法', 83.00);
INSERT INTO `user_course` VALUES (67, 220006, 'Java课程设计', 92.00);
INSERT INTO `user_course` VALUES (68, 220006, 'JavaEE企业开发', 67.00);
INSERT INTO `user_course` VALUES (69, 220007, '大数据程序设计(Python)', 75.00);
INSERT INTO `user_course` VALUES (70, 220007, '数据结构与算法', 91.00);
INSERT INTO `user_course` VALUES (71, 220007, '软件工程', 57.00);
INSERT INTO `user_course` VALUES (72, 220007, '计算机网络原理', 77.00);
INSERT INTO `user_course` VALUES (73, 220007, '程序设计基础(网)', 100.00);
INSERT INTO `user_course` VALUES (74, 220007, 'Linux编程及应用', 98.00);
INSERT INTO `user_course` VALUES (75, 220007, 'WEB前端开发', 95.00);
INSERT INTO `user_course` VALUES (76, 220007, '机械趣味模型', 94.00);
INSERT INTO `user_course` VALUES (77, 220007, '应用微生物学', 90.00);
INSERT INTO `user_course` VALUES (78, 220007, '创新性思维与方法', 78.00);
INSERT INTO `user_course` VALUES (79, 220007, 'Java课程设计', 88.00);
INSERT INTO `user_course` VALUES (80, 220007, 'JavaEE企业开发', 67.00);
INSERT INTO `user_course` VALUES (81, 220008, '大数据程序设计(Python)', 64.00);
INSERT INTO `user_course` VALUES (82, 220008, '数据结构与算法', 94.00);
INSERT INTO `user_course` VALUES (83, 220008, '软件工程', 88.00);
INSERT INTO `user_course` VALUES (84, 220008, '计算机网络原理', 55.00);
INSERT INTO `user_course` VALUES (85, 220008, '程序设计基础(网)', 93.00);
INSERT INTO `user_course` VALUES (86, 220008, 'Linux编程及应用', 96.00);
INSERT INTO `user_course` VALUES (87, 220008, 'WEB前端开发', 97.00);
INSERT INTO `user_course` VALUES (88, 220008, '机械趣味模型', 62.00);
INSERT INTO `user_course` VALUES (89, 220008, '应用微生物学', 65.00);
INSERT INTO `user_course` VALUES (90, 220008, '创新性思维与方法', 78.00);
INSERT INTO `user_course` VALUES (91, 220008, 'Java课程设计', 52.00);
INSERT INTO `user_course` VALUES (92, 220008, 'JavaEE企业开发', 91.00);
INSERT INTO `user_course` VALUES (93, 220009, '大数据程序设计(Python)', 61.00);
INSERT INTO `user_course` VALUES (94, 220009, '数据结构与算法', 99.00);
INSERT INTO `user_course` VALUES (95, 220009, '软件工程', 94.00);
INSERT INTO `user_course` VALUES (96, 220009, '计算机网络原理', 69.00);
INSERT INTO `user_course` VALUES (97, 220009, '程序设计基础(网)', 69.00);
INSERT INTO `user_course` VALUES (98, 220009, 'Linux编程及应用', 92.00);
INSERT INTO `user_course` VALUES (99, 220009, 'WEB前端开发', 74.00);
INSERT INTO `user_course` VALUES (100, 220009, '机械趣味模型', 74.00);
INSERT INTO `user_course` VALUES (101, 220009, '应用微生物学', 97.00);
INSERT INTO `user_course` VALUES (102, 220009, '创新性思维与方法', 72.00);
INSERT INTO `user_course` VALUES (103, 220009, 'Java课程设计', 90.00);
INSERT INTO `user_course` VALUES (104, 220009, 'JavaEE企业开发', 96.00);
INSERT INTO `user_course` VALUES (105, 220010, '大数据程序设计(Python)', 84.00);
INSERT INTO `user_course` VALUES (106, 220010, '数据结构与算法', 79.00);
INSERT INTO `user_course` VALUES (107, 220010, '软件工程', 81.00);
INSERT INTO `user_course` VALUES (108, 220010, '计算机网络原理', 69.00);
INSERT INTO `user_course` VALUES (109, 220010, '程序设计基础(网)', 77.00);
INSERT INTO `user_course` VALUES (110, 220010, 'Linux编程及应用', 57.00);
INSERT INTO `user_course` VALUES (111, 220010, 'WEB前端开发', 51.00);
INSERT INTO `user_course` VALUES (112, 220010, '机械趣味模型', 99.00);
INSERT INTO `user_course` VALUES (113, 220010, '应用微生物学', 67.00);
INSERT INTO `user_course` VALUES (114, 220010, '创新性思维与方法', 86.00);
INSERT INTO `user_course` VALUES (115, 220010, 'Java课程设计', 62.00);
INSERT INTO `user_course` VALUES (116, 220010, 'JavaEE企业开发', 70.00);
INSERT INTO `user_course` VALUES (117, 220011, '大数据程序设计(Python)', 80.00);
INSERT INTO `user_course` VALUES (118, 220011, '数据结构与算法', 64.00);
INSERT INTO `user_course` VALUES (119, 220011, '软件工程', 92.00);
INSERT INTO `user_course` VALUES (120, 220011, '计算机网络原理', 86.00);
INSERT INTO `user_course` VALUES (121, 220011, '程序设计基础(网)', 95.00);
INSERT INTO `user_course` VALUES (122, 220011, 'Linux编程及应用', 76.00);
INSERT INTO `user_course` VALUES (123, 220011, 'WEB前端开发', 57.00);
INSERT INTO `user_course` VALUES (124, 220011, '机械趣味模型', 69.00);
INSERT INTO `user_course` VALUES (125, 220011, '应用微生物学', 79.00);
INSERT INTO `user_course` VALUES (126, 220011, '创新性思维与方法', 52.00);
INSERT INTO `user_course` VALUES (127, 220011, 'Java课程设计', 71.00);
INSERT INTO `user_course` VALUES (128, 220011, 'JavaEE企业开发', 78.00);
INSERT INTO `user_course` VALUES (129, 220012, '大数据程序设计(Python)', 92.00);
INSERT INTO `user_course` VALUES (130, 220012, '数据结构与算法', 81.00);
INSERT INTO `user_course` VALUES (131, 220012, '软件工程', 84.00);
INSERT INTO `user_course` VALUES (132, 220012, '计算机网络原理', 93.00);
INSERT INTO `user_course` VALUES (133, 220012, '程序设计基础(网)', 58.00);
INSERT INTO `user_course` VALUES (134, 220012, 'Linux编程及应用', 97.00);
INSERT INTO `user_course` VALUES (135, 220012, 'WEB前端开发', 76.00);
INSERT INTO `user_course` VALUES (136, 220012, '机械趣味模型', 98.00);
INSERT INTO `user_course` VALUES (137, 220012, '应用微生物学', 80.00);
INSERT INTO `user_course` VALUES (138, 220012, '创新性思维与方法', 75.00);
INSERT INTO `user_course` VALUES (139, 220012, 'Java课程设计', 66.00);
INSERT INTO `user_course` VALUES (140, 220012, 'JavaEE企业开发', 60.00);
INSERT INTO `user_course` VALUES (141, 220013, '大数据程序设计(Python)', 53.00);
INSERT INTO `user_course` VALUES (142, 220013, '数据结构与算法', 77.00);
INSERT INTO `user_course` VALUES (143, 220013, '软件工程', 83.00);
INSERT INTO `user_course` VALUES (144, 220013, '计算机网络原理', 52.00);
INSERT INTO `user_course` VALUES (145, 220013, '程序设计基础(网)', 97.00);
INSERT INTO `user_course` VALUES (146, 220013, 'Linux编程及应用', 86.00);
INSERT INTO `user_course` VALUES (147, 220013, 'WEB前端开发', 63.00);
INSERT INTO `user_course` VALUES (148, 220013, '机械趣味模型', 87.00);
INSERT INTO `user_course` VALUES (149, 220013, '应用微生物学', 100.00);
INSERT INTO `user_course` VALUES (150, 220013, '创新性思维与方法', 88.00);
INSERT INTO `user_course` VALUES (151, 220013, 'Java课程设计', 65.00);
INSERT INTO `user_course` VALUES (152, 220013, 'JavaEE企业开发', 87.00);
INSERT INTO `user_course` VALUES (153, 220014, '大数据程序设计(Python)', 74.00);
INSERT INTO `user_course` VALUES (154, 220014, '数据结构与算法', 60.00);
INSERT INTO `user_course` VALUES (155, 220014, '软件工程', 58.00);
INSERT INTO `user_course` VALUES (156, 220014, '计算机网络原理', 64.00);
INSERT INTO `user_course` VALUES (157, 220014, '程序设计基础(网)', 91.00);
INSERT INTO `user_course` VALUES (158, 220014, 'Linux编程及应用', 84.00);
INSERT INTO `user_course` VALUES (159, 220014, 'WEB前端开发', 68.00);
INSERT INTO `user_course` VALUES (160, 220014, '机械趣味模型', 56.00);
INSERT INTO `user_course` VALUES (161, 220014, '应用微生物学', 89.00);
INSERT INTO `user_course` VALUES (162, 220014, '创新性思维与方法', 71.00);
INSERT INTO `user_course` VALUES (163, 220014, 'Java课程设计', 50.00);
INSERT INTO `user_course` VALUES (164, 220014, 'JavaEE企业开发', 51.00);
INSERT INTO `user_course` VALUES (165, 220015, '大数据程序设计(Python)', 90.00);
INSERT INTO `user_course` VALUES (166, 220015, '数据结构与算法', 72.00);
INSERT INTO `user_course` VALUES (167, 220015, '软件工程', 52.00);
INSERT INTO `user_course` VALUES (168, 220015, '计算机网络原理', 72.00);
INSERT INTO `user_course` VALUES (169, 220015, '程序设计基础(网)', 66.00);
INSERT INTO `user_course` VALUES (170, 220015, 'Linux编程及应用', 66.00);
INSERT INTO `user_course` VALUES (171, 220015, 'WEB前端开发', 75.00);
INSERT INTO `user_course` VALUES (172, 220015, '机械趣味模型', 61.00);
INSERT INTO `user_course` VALUES (173, 220015, '应用微生物学', 86.00);
INSERT INTO `user_course` VALUES (174, 220015, '创新性思维与方法', 53.00);
INSERT INTO `user_course` VALUES (175, 220015, 'Java课程设计', 82.00);
INSERT INTO `user_course` VALUES (176, 220015, 'JavaEE企业开发', 79.00);
INSERT INTO `user_course` VALUES (177, 220016, '大数据程序设计(Python)', 87.00);
INSERT INTO `user_course` VALUES (178, 220016, '数据结构与算法', 88.00);
INSERT INTO `user_course` VALUES (179, 220016, '软件工程', 51.00);
INSERT INTO `user_course` VALUES (180, 220016, '计算机网络原理', 95.00);
INSERT INTO `user_course` VALUES (181, 220016, '程序设计基础(网)', 100.00);
INSERT INTO `user_course` VALUES (182, 220016, 'Linux编程及应用', 57.00);
INSERT INTO `user_course` VALUES (183, 220016, 'WEB前端开发', 85.00);
INSERT INTO `user_course` VALUES (184, 220016, '机械趣味模型', 100.00);
INSERT INTO `user_course` VALUES (185, 220016, '应用微生物学', 93.00);
INSERT INTO `user_course` VALUES (186, 220016, '创新性思维与方法', 50.00);
INSERT INTO `user_course` VALUES (187, 220016, 'Java课程设计', 69.00);
INSERT INTO `user_course` VALUES (188, 220016, 'JavaEE企业开发', 95.00);
INSERT INTO `user_course` VALUES (189, 220017, '大数据程序设计(Python)', 52.00);
INSERT INTO `user_course` VALUES (190, 220017, '数据结构与算法', 62.00);
INSERT INTO `user_course` VALUES (191, 220017, '软件工程', 60.00);
INSERT INTO `user_course` VALUES (192, 220017, '计算机网络原理', 85.00);
INSERT INTO `user_course` VALUES (193, 220017, '程序设计基础(网)', 58.00);
INSERT INTO `user_course` VALUES (194, 220017, 'Linux编程及应用', 90.00);
INSERT INTO `user_course` VALUES (195, 220017, 'WEB前端开发', 93.00);
INSERT INTO `user_course` VALUES (196, 220017, '机械趣味模型', 91.00);
INSERT INTO `user_course` VALUES (197, 220017, '应用微生物学', 63.00);
INSERT INTO `user_course` VALUES (198, 220017, '创新性思维与方法', 67.00);
INSERT INTO `user_course` VALUES (199, 220017, 'Java课程设计', 73.00);
INSERT INTO `user_course` VALUES (200, 220017, 'JavaEE企业开发', 73.00);
INSERT INTO `user_course` VALUES (201, 220018, '大数据程序设计(Python)', 60.00);
INSERT INTO `user_course` VALUES (202, 220018, '数据结构与算法', 65.00);
INSERT INTO `user_course` VALUES (203, 220018, '软件工程', 60.00);
INSERT INTO `user_course` VALUES (204, 220018, '计算机网络原理', 50.00);
INSERT INTO `user_course` VALUES (205, 220018, '程序设计基础(网)', 52.00);
INSERT INTO `user_course` VALUES (206, 220018, 'Linux编程及应用', 56.00);
INSERT INTO `user_course` VALUES (207, 220018, 'WEB前端开发', 71.00);
INSERT INTO `user_course` VALUES (208, 220018, '机械趣味模型', 61.00);
INSERT INTO `user_course` VALUES (209, 220018, '应用微生物学', 79.00);
INSERT INTO `user_course` VALUES (210, 220018, '创新性思维与方法', 67.00);
INSERT INTO `user_course` VALUES (211, 220018, 'Java课程设计', 98.00);
INSERT INTO `user_course` VALUES (212, 220018, 'JavaEE企业开发', 90.00);
INSERT INTO `user_course` VALUES (213, 220019, '大数据程序设计(Python)', 72.00);
INSERT INTO `user_course` VALUES (214, 220019, '数据结构与算法', 93.00);
INSERT INTO `user_course` VALUES (215, 220019, '软件工程', 89.00);
INSERT INTO `user_course` VALUES (216, 220019, '计算机网络原理', 97.00);
INSERT INTO `user_course` VALUES (217, 220019, '程序设计基础(网)', 75.00);
INSERT INTO `user_course` VALUES (218, 220019, 'Linux编程及应用', 60.00);
INSERT INTO `user_course` VALUES (219, 220019, 'WEB前端开发', 95.00);
INSERT INTO `user_course` VALUES (220, 220019, '机械趣味模型', 70.00);
INSERT INTO `user_course` VALUES (221, 220019, '应用微生物学', 81.00);
INSERT INTO `user_course` VALUES (222, 220019, '创新性思维与方法', 60.00);
INSERT INTO `user_course` VALUES (223, 220019, 'Java课程设计', 85.00);
INSERT INTO `user_course` VALUES (224, 220019, 'JavaEE企业开发', 52.00);
INSERT INTO `user_course` VALUES (225, 220020, '大数据程序设计(Python)', 89.00);
INSERT INTO `user_course` VALUES (226, 220020, '数据结构与算法', 58.00);
INSERT INTO `user_course` VALUES (227, 220020, '软件工程', 91.00);
INSERT INTO `user_course` VALUES (228, 220020, '计算机网络原理', 99.00);
INSERT INTO `user_course` VALUES (229, 220020, '程序设计基础(网)', 62.00);
INSERT INTO `user_course` VALUES (230, 220020, 'Linux编程及应用', 91.00);
INSERT INTO `user_course` VALUES (231, 220020, 'WEB前端开发', 82.00);
INSERT INTO `user_course` VALUES (232, 220020, '机械趣味模型', 97.00);
INSERT INTO `user_course` VALUES (233, 220020, '应用微生物学', 56.00);
INSERT INTO `user_course` VALUES (234, 220020, '创新性思维与方法', 81.00);
INSERT INTO `user_course` VALUES (235, 220020, 'Java课程设计', 75.00);
INSERT INTO `user_course` VALUES (236, 220020, 'JavaEE企业开发', 89.00);
INSERT INTO `user_course` VALUES (237, 220021, '大数据程序设计(Python)', 80.00);
INSERT INTO `user_course` VALUES (238, 220021, '数据结构与算法', 88.00);
INSERT INTO `user_course` VALUES (239, 220021, '软件工程', 63.00);
INSERT INTO `user_course` VALUES (240, 220021, '计算机网络原理', 68.00);
INSERT INTO `user_course` VALUES (241, 220021, '程序设计基础(网)', 64.00);
INSERT INTO `user_course` VALUES (242, 220021, 'Linux编程及应用', 64.00);
INSERT INTO `user_course` VALUES (243, 220021, 'WEB前端开发', 98.00);
INSERT INTO `user_course` VALUES (244, 220021, '机械趣味模型', 72.00);
INSERT INTO `user_course` VALUES (245, 220021, '应用微生物学', 56.00);
INSERT INTO `user_course` VALUES (246, 220021, '创新性思维与方法', 69.00);
INSERT INTO `user_course` VALUES (247, 220021, 'Java课程设计', 63.00);
INSERT INTO `user_course` VALUES (248, 220021, 'JavaEE企业开发', 96.00);
INSERT INTO `user_course` VALUES (249, 220022, '大数据程序设计(Python)', 50.00);
INSERT INTO `user_course` VALUES (250, 220022, '数据结构与算法', 70.00);
INSERT INTO `user_course` VALUES (251, 220022, '软件工程', 77.00);
INSERT INTO `user_course` VALUES (252, 220022, '计算机网络原理', 76.00);
INSERT INTO `user_course` VALUES (253, 220022, '程序设计基础(网)', 92.00);
INSERT INTO `user_course` VALUES (254, 220022, 'Linux编程及应用', 79.00);
INSERT INTO `user_course` VALUES (255, 220022, 'WEB前端开发', 67.00);
INSERT INTO `user_course` VALUES (256, 220022, '机械趣味模型', 68.00);
INSERT INTO `user_course` VALUES (257, 220022, '应用微生物学', 70.00);
INSERT INTO `user_course` VALUES (258, 220022, '创新性思维与方法', 67.00);
INSERT INTO `user_course` VALUES (259, 220022, 'Java课程设计', 86.00);
INSERT INTO `user_course` VALUES (260, 220022, 'JavaEE企业开发', 77.00);
INSERT INTO `user_course` VALUES (261, 220023, '大数据程序设计(Python)', 77.00);
INSERT INTO `user_course` VALUES (262, 220023, '数据结构与算法', 55.00);
INSERT INTO `user_course` VALUES (263, 220023, '软件工程', 61.00);
INSERT INTO `user_course` VALUES (264, 220023, '计算机网络原理', 52.00);
INSERT INTO `user_course` VALUES (265, 220023, '程序设计基础(网)', 74.00);
INSERT INTO `user_course` VALUES (266, 220023, 'Linux编程及应用', 80.00);
INSERT INTO `user_course` VALUES (267, 220023, 'WEB前端开发', 71.00);
INSERT INTO `user_course` VALUES (268, 220023, '机械趣味模型', 55.00);
INSERT INTO `user_course` VALUES (269, 220023, '应用微生物学', 79.00);
INSERT INTO `user_course` VALUES (270, 220023, '创新性思维与方法', 84.00);
INSERT INTO `user_course` VALUES (271, 220023, 'Java课程设计', 56.00);
INSERT INTO `user_course` VALUES (272, 220023, 'JavaEE企业开发', 57.00);
INSERT INTO `user_course` VALUES (273, 220024, '大数据程序设计(Python)', 66.00);
INSERT INTO `user_course` VALUES (274, 220024, '数据结构与算法', 76.00);
INSERT INTO `user_course` VALUES (275, 220024, '软件工程', 90.00);
INSERT INTO `user_course` VALUES (276, 220024, '计算机网络原理', 89.00);
INSERT INTO `user_course` VALUES (277, 220024, '程序设计基础(网)', 51.00);
INSERT INTO `user_course` VALUES (278, 220024, 'Linux编程及应用', 99.00);
INSERT INTO `user_course` VALUES (279, 220024, 'WEB前端开发', 57.00);
INSERT INTO `user_course` VALUES (280, 220024, '机械趣味模型', 73.00);
INSERT INTO `user_course` VALUES (281, 220024, '应用微生物学', 84.00);
INSERT INTO `user_course` VALUES (282, 220024, '创新性思维与方法', 53.00);
INSERT INTO `user_course` VALUES (283, 220024, 'Java课程设计', 87.00);
INSERT INTO `user_course` VALUES (284, 220024, 'JavaEE企业开发', 62.00);
INSERT INTO `user_course` VALUES (285, 220025, '大数据程序设计(Python)', 86.00);
INSERT INTO `user_course` VALUES (286, 220025, '数据结构与算法', 83.00);
INSERT INTO `user_course` VALUES (287, 220025, '软件工程', 72.00);
INSERT INTO `user_course` VALUES (288, 220025, '计算机网络原理', 87.00);
INSERT INTO `user_course` VALUES (289, 220025, '程序设计基础(网)', 94.00);
INSERT INTO `user_course` VALUES (290, 220025, 'Linux编程及应用', 82.00);
INSERT INTO `user_course` VALUES (291, 220025, 'WEB前端开发', 62.00);
INSERT INTO `user_course` VALUES (292, 220025, '机械趣味模型', 88.00);
INSERT INTO `user_course` VALUES (293, 220025, '应用微生物学', 79.00);
INSERT INTO `user_course` VALUES (294, 220025, '创新性思维与方法', 84.00);
INSERT INTO `user_course` VALUES (295, 220025, 'Java课程设计', 99.00);
INSERT INTO `user_course` VALUES (296, 220025, 'JavaEE企业开发', 96.00);
INSERT INTO `user_course` VALUES (297, 220001, '大数据程序设计(Python)', 75.00);
INSERT INTO `user_course` VALUES (298, 220001, '数据结构与算法', 99.00);
INSERT INTO `user_course` VALUES (299, 220001, '软件工程', 71.00);
INSERT INTO `user_course` VALUES (300, 220001, '计算机网络原理', 59.00);
INSERT INTO `user_course` VALUES (301, 220001, '程序设计基础(网)', 61.00);
INSERT INTO `user_course` VALUES (302, 220001, 'Linux编程及应用', 79.00);
INSERT INTO `user_course` VALUES (303, 220001, 'WEB前端开发', 61.00);
INSERT INTO `user_course` VALUES (304, 220001, '机械趣味模型', 52.00);
INSERT INTO `user_course` VALUES (305, 220001, '应用微生物学', 54.00);
INSERT INTO `user_course` VALUES (306, 220001, '创新性思维与方法', 91.00);
INSERT INTO `user_course` VALUES (307, 220001, 'Java课程设计', 86.00);
INSERT INTO `user_course` VALUES (308, 220001, 'JavaEE企业开发', 57.00);
INSERT INTO `user_course` VALUES (309, 220002, '大数据程序设计(Python)', 90.00);
INSERT INTO `user_course` VALUES (310, 220002, '数据结构与算法', 81.00);
INSERT INTO `user_course` VALUES (311, 220002, '软件工程', 75.00);
INSERT INTO `user_course` VALUES (312, 220002, '计算机网络原理', 89.00);
INSERT INTO `user_course` VALUES (313, 220002, '程序设计基础(网)', 58.00);
INSERT INTO `user_course` VALUES (314, 220002, 'Linux编程及应用', 94.00);
INSERT INTO `user_course` VALUES (315, 220002, 'WEB前端开发', 90.00);
INSERT INTO `user_course` VALUES (316, 220002, '机械趣味模型', 75.00);
INSERT INTO `user_course` VALUES (317, 220002, '应用微生物学', 55.00);
INSERT INTO `user_course` VALUES (318, 220002, '创新性思维与方法', 66.00);
INSERT INTO `user_course` VALUES (319, 220002, 'Java课程设计', 91.00);
INSERT INTO `user_course` VALUES (320, 220002, 'JavaEE企业开发', 70.00);

SET FOREIGN_KEY_CHECKS = 1;
