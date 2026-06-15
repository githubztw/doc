package com.example.app.architecture;

import com.tngtech.archunit.core.importer.ImportOption;
import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.library.Architectures.layeredArchitecture;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

@AnalyzeClasses(
    packages = "com.example.app",
    importOptions = ImportOption.DoNotIncludeTests.class
)
public class LayerDependencyTest {

    @ArchTest
    public static final ArchRule layered = layeredArchitecture()
        .consideringAllDependencies()
        .layer("Domain").definedBy("..domain..") //领域层
        .layer("Config").definedBy("..config..") //配置层
        .layer("Mapper").definedBy("..mapper..") //映射层
        .layer("Service").definedBy("..service..") //服务层
        .layer("Controller").definedBy("..controller..") //控制层
        .layer("Infrastructure").definedBy("..infrastructure..") //基础设施层
        .whereLayer("Controller").mayNotBeAccessedByAnyLayer() //controller 不能被其他层访问
        .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller") //service 只能被 controller 访问
        .whereLayer("Mapper").mayOnlyBeAccessedByLayers("Service") //mapper 只能被 service 访问
        .whereLayer("Domain").mayOnlyBeAccessedByLayers("Config") //domain 只能被 config 访问
        .whereLayer("Config").mayOnlyBeAccessedByLayers("Mapper") //config 只能被 mapper 访问
        .whereLayer("Mapper").mayOnlyBeAccessedByLayers("Service") //mapper 只能被 service 访问
        .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller") //service 只能被 controller 访问
        .whereLayer("Controller").mayNotBeAccessedByAnyLayer() //controller 不能被其他层访问
        .as(
            "❌ 层级依赖违规。\n" +
            "✅ FIX: Controller 必须经 Service, Service 通过 MyBatis-Plus Mapper 访问数据。\n" +
            "📖 See: docs/architecture/boundaries.md"
        );

    @ArchTest
    public static final ArchRule controllerMustNotUseMapper = noClasses()
        .that().resideInAPackage("..controller..")
        .should().dependOnClassesThat().resideInAPackage("..mapper..")
        .as(
            "❌ Controller 不得直接依赖 Mapper。\n" +
            "✅ FIX: 在 Service 中编排数据访问, Controller 仅持有 Service 引用。\n" +
            "📖 See: docs/architecture/boundaries.md"
        );

    @ArchTest
    public static final ArchRule noFieldInjection = noClasses()
        .should().beAnnotatedWith("org.springframework.beans.factory.annotation.Autowired")
        .as(
            "❌ 禁止字段级 @Autowired。\n" +
            "✅ FIX: 构造器注入:\n" +
            "    @RequiredArgsConstructor\n" +
            "    public class UserService {\n" +
            "        private final UserMapper userMapper;\n" +
            "    }\n" +
            "📖 See: docs/conventions/di.md"
        );
}
