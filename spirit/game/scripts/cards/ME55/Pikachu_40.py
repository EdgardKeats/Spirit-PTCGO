from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3d0d3fe-2045-557c-ab25-24a3c79fc25a",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Overwriting Bolt",
            game_text="The Defending Pok\u00e9mon's Weakness is now Lightning until the end of your next turn. (Apply Weakness as x2.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)