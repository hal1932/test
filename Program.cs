using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.Formatting;
using Microsoft.CodeAnalysis.MSBuild;
using System;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            // http://dogschasingsquirrels.com/2014/08/04/code-generation-with-roslyn-fields-and-properties/
            // http://yupotown.ldblog.jp/archives/44318776.html
            // http://mousouprogrammer.blogspot.jp/2014/09/roslynsyntaxnode.html
            var klass = SyntaxFactory.ClassDeclaration("TestClass")
                .AddModifiers(SyntaxFactory.Token(SyntaxKind.PublicKeyword))
                .AddMembers(
                    SyntaxFactory.PropertyDeclaration(SyntaxFactory.ParseTypeName("int"), "PropInt")
                        .AddModifiers(SyntaxFactory.Token(SyntaxKind.PublicKeyword))
                        .AddAccessorListAccessors(
                            SyntaxFactory.AccessorDeclaration(SyntaxKind.GetAccessorDeclaration)
                                .WithSemicolonToken(SyntaxFactory.Token(SyntaxKind.SemicolonToken)),
                            SyntaxFactory.AccessorDeclaration(SyntaxKind.SetAccessorDeclaration)
                                .WithSemicolonToken(SyntaxFactory.Token(SyntaxKind.SemicolonToken)))
                    );

            var workspace = MSBuildWorkspace.Create();
            Console.WriteLine(Formatter.Format(klass, workspace));
            Console.Read();
        }
    }
}
